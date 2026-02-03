const FAKE_RESULTS = {
  youtube: [
    "Learn Flask in 15 Minutes",
    "Study Music - 집중 집중",
    "Cyber Awareness 101",
    "Beginner Python Projects",
  ],
  google: [
    "Official University Portal",
    "Library Resources and Journals",
    "Cyber Safety Guidelines",
    "Student Login Page",
  ],
  amazon: [
    "Wireless Earbuds - Student Deal",
    "Laptop Stand - Ergonomic",
    "Notebook Pack - 6 Items",
    "USB-C Hub - 7-in-1",
  ],
};

function handleFakeSearch(event, site) {
  event.preventDefault();
  const input = document.getElementById(`${site}-search`);
  const resultsBox = document.getElementById(`${site}-results`);
  if (!input || !resultsBox) {
    return false;
  }

  const query = input.value.trim();
  if (!query) {
    resultsBox.innerHTML = "<p>Please enter a search term.</p>";
    return false;
  }

  const items = FAKE_RESULTS[site] || [];
  const filtered = items.filter((item) =>
    item.toLowerCase().includes(query.toLowerCase())
  );

  const list = filtered.length ? filtered : items;
  const rendered = list
    .map((item) => `<li>${item}</li>`)
    .join("");

  resultsBox.innerHTML = `
    <h3>Showing results for "${query}"</h3>
    <ul>${rendered}</ul>
    <p class="small-note">Results are simulated inside the decoy environment.</p>
  `;

  return false;
}

function fillLucky(inputId) {
  const input = document.getElementById(inputId);
  if (input) {
    input.value = "student portal";
    input.focus();
  }
}
