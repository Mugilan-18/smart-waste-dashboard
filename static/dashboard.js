setInterval(()=>{
fetch("/api/data")
.then(r=>r.json())
.then(res=>{
let body=document.getElementById("table-body");
if(res.status==="NO_DATA"){
body.innerHTML="<tr><td colspan='5'>No ESP Data received yet</td></tr>";
return;
}
let d=res.data;
let status="NORMAL";
if(d.gas>300 || d.level>80) status="CRITICAL";
else if(d.gas>200 || d.level>60) status="WARNING";

body.innerHTML=`
<tr>
<td>${d.bin_id}</td>
<td>${d.area}</td>
<td>${d.gas}</td>
<td>${d.level}</td>
<td>${status}</td>
</tr>`;
});
},2000);

