setInterval(() => {
  fetch("/api/data")
    .then(res => res.json())
    .then(d => {
      if (!d) return;

      let status = "NORMAL";
      if (d.gas > 400 || d.level > 90) status = "CRITICAL";
      else if (d.gas > 250 || d.level > 70) status = "WARNING";

      document.getElementById("data-row").innerHTML = `
        <tr>
          <td>${d.bin_id}</td>
          <td>${d.area}</td>
          <td>${d.gas}</td>
          <td>${d.level}</td>
          <td class="${status.toLowerCase()}">${status}</td>
        </tr>
      `;
    });
}, 2000);   // 2 sec → smooth real-time
