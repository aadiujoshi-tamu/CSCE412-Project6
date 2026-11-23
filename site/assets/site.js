fetch("release.json").then((response) => response.json()).then((release) => {
  document.querySelector("#release-id").textContent = release.commit_sha;
}).catch(() => { document.querySelector("#release-id").textContent = "unavailable"; });
