setInterval(fetchData, 2000);

function fetchData() {
    fetch("/api/data")
        .then(res => res.json())
        .then(res => {

            const system = document.getElementById("system");
            const totalBins = document.getElementById("totalBins");
            const table = document.getElementById("tableBody");

            if (!res.connected) {
                system.innerText = "Connection Lost";
                system.className = "card red";
                totalBins.innerText = "Total Bins: 0";
                table.innerHTML =
                    `<tr class="no-data">
                        <td colspan="5">No ESP Data received yet</td>
                     </tr>`;
                return;
            }

            system.innerText = "System ONLINE";
            system.className = "card blue";
            totalBins.innerText = "Total Bins: 1";

            const d = res.data;

            let status = "NORMAL";
            if (d.gas > 300 || d.level > 90) status = "CRITICAL";
            else if (d.gas > 150 || d.level > 70) status = "WARNING";

            table.innerHTML = `
                <tr>
                    <td>${d.bin_id}</td>
                    <td>${d.area}</td>
                    <td>${d.gas}</td>
                    <td>${d.level}%</td>
                    <td>${status}</td>
                </tr>`;
        })
        .catch(() => {
            document.getElementById("system").innerText = "Connection Lost";
            document.getElementById("system").className = "card red";
        });
}
