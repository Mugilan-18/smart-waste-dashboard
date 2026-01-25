function startLive() {
  setInterval(fetchData, 1000); // 1 second
}

function fetchData() {
  fetch("/api/data")
    .then(res => res.json())
    .then(data => {

      if (data.status === "no_data") return;

      document.getElementById("tableBody").innerHTML = `
        <tr class="${data.status}">
          <td>${data.bin_id}</td>
          <td>${data.area}</td>
          <td>${data.gas}</td>
          <td>${data.level}%</td>
          <td>${data.status}</td>
        </tr>
      `;
    });
}
