setInterval(()=>{
  fetch("/api/data")
  .then(res=>res.json())
  .then(d=>{
    document.getElementById("bin_id").innerText = d.bin_id;
    document.getElementById("area").innerText = d.area;
    document.getElementById("gas").innerText = d.gas;
    document.getElementById("level").innerText = d.level;
    document.getElementById("status").innerText = d.status;
  });
},2000);
