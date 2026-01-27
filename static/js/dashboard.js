setInterval(fetchData,2000);

function fetchData(){
fetch("/api/data")
.then(r=>r.json())
.then(res=>{
 const sys=document.getElementById("system");

 if(!res.connected){
   sys.innerText="Connection Lost";
   sys.style.background="red";
   showNoData();
   return;
 }

 const d=res.data;
 sys.innerText="System ONLINE";
 sys.style.background="blue";

 document.getElementById("totalBins").innerText="Total Bins: "+d.total_bins;

 let status="NORMAL";
 if(d.gas>300||d.level>90) status="CRITICAL";
 else if(d.gas>150||d.level>70) status="WARNING";

 document.getElementById("tableBody").innerHTML=`
 <tr>
 <td>${d.bin_id}</td>
 <td>${d.area}</td>
 <td>${d.gas}</td>
 <td>${d.level}%</td>
 <td>${status}</td>
 </tr>`;
});
}

function showNoData(){
document.getElementById("tableBody").innerHTML=
`<tr class="no-data"><td colspan="5">No ESP Data received yet</td></tr>`;
}
