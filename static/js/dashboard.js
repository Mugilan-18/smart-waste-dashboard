setInterval(()=>{
fetch("/api/data")
.then(r=>r.json())
.then(res=>{
    const table = document.getElementById("table-body");
    const system = document.getElementById("system");

    if(!res.connected){
        system.innerText = "Connection Lost";
        system.className = "status-box red";
        table.innerHTML = "<tr><td colspan='5' class='no-data'>Data Not Received</td></tr>";
        return;
    }

    system.innerText = "System ONLINE";
    system.className = "status-box blue";

    const d = res.data;
    let status = "NORMAL";
    if(d.gas > 300 || d.level > 80) status = "CRITICAL";
    else if(d.gas > 200 || d.level > 60) status = "WARNING";

    table.innerHTML = `
    <tr>
        <td>${d.bin_id}</td>
        <td>${d.area}</td>
        <td>${d.gas}</td>
        <td>${d.level}%</td>
        <td>${status}</td>
    </tr>`;
});
},2000);
