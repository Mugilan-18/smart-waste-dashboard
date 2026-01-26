async function loadData(){
  const r = await fetch("/api/data");
  const d = await r.json();

  document.getElementById("bin_id").innerText = d.bin_id || "-";
  document.getElementById("area").innerText = d.area || "-";
  document.getElementById("gas").innerText = d.gas || 0;
  document.getElementById("level").innerText = d.bin_level || 0;

  document.getElementById("system").innerHTML = "System<br>" + d.system_status;
  document.getElementById("monitor").innerHTML = "Monitoring<br>" + d.monitoring;

  let status = "NORMAL";
  let color = "green";

  if (d.bin_level > 80 || d.gas > 300) {
    status = "CRITICAL"; color = "red";
  } else if (d.bin_level > 60) {
    status = "WARNING"; color = "orange";
  }

  let s = document.getElementById("status");
  s.innerText = status;
  s.style.color = color;
}

setInterval(loadData, 2000);
loadData();
