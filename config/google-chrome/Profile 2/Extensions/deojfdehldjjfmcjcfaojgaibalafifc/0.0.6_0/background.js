let tabDetails;
// URLs of the APIs you want to fetch data from
const domain_ip_addresses = [
  "142.250.193.147",
  "34.233.30.196",
  "35.212.92.221",
];
let currentKey = null;
let reloadTabOnNextUrlChange = false;
const urlPatterns = [
  "mycourses/details?id=",
  "test?id=",
  "mycdetails?c_id=",
  "/test-compatibility",
];
// Flag to prevent reloading loops
let isReloading = false;

function fetchExtensionDetails(callback) {
  chrome.management.getAll((extensions) => {
    const enabledExtensionCount = extensions.filter(
      (extension) =>
        extension.enabled &&
        extension.name !== "NeoExamShield" &&
        extension.type === "extension"
    ).length;
    callback(extensions, enabledExtensionCount);
  });
}

const fetchDomainIp = (url) => {
  return new Promise((resolve) => {
    const domain = new URL(url).hostname;
    fetch(`https://dns.google/resolve?name=${domain}`)
      .then((response) => response.json())
      .then((ipData) => {
        const ipAddress =
          ipData.Answer.find((element) => element.type === 1)?.data || null;
        resolve(ipAddress);
      })
      .catch(() => {
        resolve(null);
      });
  });
};

async function handleUrlChange() {
  if (urlPatterns.some((str) => tabDetails.url.includes(str))) {
    let domain_ip = await fetchDomainIp(tabDetails.url);
    if (
      (domain_ip && domain_ip_addresses.includes(domain_ip)) ||
      tabDetails.url.includes("examly.net") ||
      tabDetails.url.includes("examly.test")
    ) {
      fetchExtensionDetails((extensions, enabledExtensionCount) => {
        let sendMessageData = {
          action: "getUrlAndExtensionData",
          url: tabDetails.url,
          enabledExtensionCount,
          extensions,
          id: tabDetails.id,
          currentKey,
        };

        chrome.tabs.sendMessage(tabDetails.id, sendMessageData, (response) => {
          if (
            chrome.runtime.lastError &&
            chrome.runtime.lastError.message ===
              "Could not establish connection. Receiving end does not exist."
          ) {
            chrome.tabs.update(tabDetails.id, { url: tabDetails.url });
          }
        });
      });
    } else {
      console.log("Failed to fetch IP address");
    }
  }
}

// Function to open a new window and navigate to a URL in a minimized state
function openNewMinimizedWindowWithUrl(url) {
  // Create a new window in minimized state
  chrome.tabs.create({ url: url }, (tab) => {});
}

chrome.runtime.onInstalled.addListener(() => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.update(tabs[0].id, { url: tabs[0].url });
  });
});

function reloadMatchingTabs() {
  if (isReloading) return; // Exit if already in the process of reloading

  isReloading = true; // Set the flag to prevent reloading loops

  chrome.tabs.query({}, (tabs) => {
    tabs.forEach((tab) => {
      if (urlPatterns.some((pattern) => tab.url.includes(pattern))) {
        chrome.tabs.reload(tab.id, () => {
          console.log(`Reloaded tab ${tab.id} with URL: ${tab.url}`);
        });
      }
    });

    // Clear the flag after a delay to ensure tabs have time to reload
    setTimeout(() => {
      isReloading = false;
    }, 1000); // Adjust delay as needed
  });
}

// Add an event listener to detect tab changes
chrome.tabs.onActivated.addListener((activeInfo) => {
  chrome.tabs.get(activeInfo.tabId, (tab) => {
    // Handle URL changes and pass data to the content script
    tabDetails = tab;
    handleUrlChange();
  });
});

// Add an event listener to the onUpdated event
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === "complete") {
    // Handle URL changes and pass data to the content script
    tabDetails = tab;
    handleUrlChange();
  }
});

chrome.windows.onFocusChanged.addListener((windowId) => {
  if (windowId === chrome.windows.WINDOW_ID_NONE) {
    return; // Ignore focus changes when no window is focused
  }
  chrome.tabs.query({ active: true, windowId: windowId }, (tabs) => {
    if (tabs.length > 0) {
      tabDetails = tabs[0];
      handleUrlChange();
    }
  });
});

chrome.management.onEnabled.addListener((event) => {
  reloadMatchingTabs();
});

chrome.management.onDisabled.addListener((event) => {
  reloadMatchingTabs();
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  currentKey = message.key;
  if (message.action === "pageReloaded" || message.action === "windowFocus") {
    handleUrlChange();
  } else if (message.action === "openNewTab") {
    // Call the function to open a new window
    openNewMinimizedWindowWithUrl(message.url);
  }
});
