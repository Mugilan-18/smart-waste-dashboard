setInterval(fetchData, 2000);

function fetchData() {
    fetch("/api/data")
        .then(res => res.json())
        .then(res => {
            if (!res.connected) {
                showNoData();
                return;
            }

            const d = res.data;
            document.getElementById("totalBins").innerText = "Total Bins: " + d.total_bins;
            document.getElementById("system").innerText = "System ONLINE";

            let status = "NORMAL";
            if (d.gas > 300 || d.level > 90) status = "CRITICAL";
            else if (d.gas > 150 || d.level > 70) status = "WARNING";

            document.getElementById("tableBody").innerHTML = `
                <tr>
                    <td>${d.bin_id}</td>
                    <td>${d.area}</td>
                    <td>${d.gas}</td>
                    <td>${d.level}%</td>
                    <td>${status}</td>
                </tr>`;
        });
}

function showNoData() {
    document.getElementById("system").innerText = "Connection Lost";
    document.getElementById("tableBody").innerHTML =
        `<tr class="no-data"><td colspan="5">No ESP Data received yet</td></tr>`;
}
