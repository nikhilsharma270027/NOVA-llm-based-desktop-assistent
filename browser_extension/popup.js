// Popup script for NOVA Activity Monitor
document.addEventListener('DOMContentLoaded', function () {
  loadTabs();

  document.getElementById('refreshBtn').addEventListener('click', function () {
    loadTabs();
  });
});

async function loadTabs() {
  try {
    // Get tabs from background script
    chrome.runtime.sendMessage({ action: "getTabs" }, function (response) {
      if (response && response.tabs) {
        displayTabs(response.tabs);
      }
    });
  } catch (error) {
    console.error("Error loading tabs:", error);
  }
}

function displayTabs(tabs) {
  const tabsList = document.getElementById('tabsList');
  const tabCount = document.getElementById('tabCount');
  const windowCount = document.getElementById('windowCount');

  // Update counts
  tabCount.textContent = tabs.length;
  const uniqueWindows = new Set(tabs.map(tab => tab.windowId));
  windowCount.textContent = uniqueWindows.size;

  // Clear existing content
  tabsList.innerHTML = '';

  if (tabs.length === 0) {
    tabsList.innerHTML = '<div style="text-align: center; opacity: 0.7;">No tabs found</div>';
    return;
  }

  // Group tabs by window
  const tabsByWindow = {};
  tabs.forEach(tab => {
    if (!tabsByWindow[tab.windowId]) {
      tabsByWindow[tab.windowId] = [];
    }
    tabsByWindow[tab.windowId].push(tab);
  });

  // Display tabs grouped by window
  Object.keys(tabsByWindow).forEach((windowId, index) => {
    const windowHeader = document.createElement('div');
    windowHeader.style.cssText = 'font-weight: bold; margin: 10px 0 5px 0; font-size: 13px;';
    windowHeader.textContent = `Window ${index + 1} (${tabsByWindow[windowId].length} tabs)`;
    tabsList.appendChild(windowHeader);

    tabsByWindow[windowId].forEach(tab => {
      const tabItem = document.createElement('div');
      tabItem.className = 'tab-item';

      const title = document.createElement('div');
      title.className = 'tab-title';
      title.textContent = tab.title || 'Untitled';
      if (tab.active) {
        title.textContent = '🔹 ' + title.textContent;
      }

      const url = document.createElement('div');
      url.className = 'tab-url';
      url.textContent = tab.url;

      tabItem.appendChild(title);
      tabItem.appendChild(url);
      tabsList.appendChild(tabItem);
    });
  });
}