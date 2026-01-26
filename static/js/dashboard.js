async function loadData() {
    const res = await fetch("/api/data");
    const data = await res.json();

    const body = document.getElementById("tableBody");

    if (!data.connected) {
        document.getElementById("totalBins").innerText = "Total Bins: 0";
        body.innerHTML = `
            <tr>
                <td colspan="5" class="no-data">
                    No ESP Data received yet
                </td>
            </tr>`;
        return;
    }

    document.getElementById("totalBins").innerText =
        "Total Bins: " + data.total_bins;

    body.innerHTML = "";

    const b = data.data;

    let status = "Normal";
    if (b.gas > 150 || b.level > 90) status = "Critical";
    else if (b.gas > 80 || b.level > 70) status = "Warning";

    body.innerHTML = `
        <tr>
            <td>${b.bin_id}</td>
            <td>${b.area}</td>
            <td>${b.gas}</td>
            <td>${b.level}%</td>
            <td>${status}</td>
        </tr>`;
}

setInterval(loadData, 2000);
loadData();
