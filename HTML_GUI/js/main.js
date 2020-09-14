function init_buttons(e)
{
    /*document.querySelector("#enableBtn").onclick = enableClick;
    document.querySelector("#enableBtn").onmouseenter = enableHover;
    document.querySelector("#enableBtn").onmouseleave = e=>{document.querySelector("#enable").hidden = true;};
    
    document.querySelector("#resetBtn").onclick = resetClick;
    document.querySelector("#resetBtn").onmouseenter = e=>{document.querySelector("#reset").hidden = false;};
    document.querySelector("#resetBtn").onmouseleave = e=>{document.querySelector("#reset").hidden = true;};
    
    document.querySelector("#calibrateBtn").onclick = calibrateClick;
    document.querySelector("#calibrateBtn").onmouseenter = e=>{document.querySelector("#calibrate").hidden = false;};
    document.querySelector("#calibrateBtn").onmouseleave = e=>{document.querySelector("#calibrate").hidden = true;};
    */
    //document.querySelector("#cameraBtn").onclick = cameraClick;
    //document.querySelector("#detectBtn").onclick = detectClick;
    /*
    document.querySelector("#enable").hidden = true;
    document.querySelector("#reset").hidden = true;
    document.querySelector("#calibrate").hidden = true;
*/
    document.querySelector("#titleFont").style.transition = "1s ease-out";
    document.querySelector("#titleFont").style.marginTop = "0";
}
window.onload = init_buttons;

function enableClick(e)
{
    let enableBtn = document.querySelector("#enableBtn");
    let enableText = document.querySelector("#enable");
    if(enableBtn.innerHTML == "Enable" || enableBtn.innerHTML == "Enable<br>Enables the drone's motors")
    {
        enableBtn.innerHTML = "Disable";
        enableText.innerHTML = "Disables the drone's motors";
    }
    else if(enableBtn.innerHTML == "Disable" || enableBtn.innerHTML == "Disable<br>Disables the drone's motors")
    {
        enableBtn.innerHTML = "Enable";
        enableText.innerHTML = "Enables the drone's motors";
    }
}
function enableHover(e)
{
    let enableBtn = document.querySelector("#enableBtn");
    let enableText = document.querySelector("#enable");
    if(enableBtn.innerHTML == "Disable")
    {
        enableText.innerHTML = "Disables the drone's motors";
    }
    else
    {
        enableText.innerHTML = "Enables the drone's motors";
    }
    enableText.hidden = false;
}

function resetClick(e)
{
    
}

function calibrateClick(e)
{
    
}

function cameraClick(e)
{
    let cameraBtn = document.querySelector("#cameraBtn");
    if(cameraBtn.innerHTML == "Turn Camera On")
    {
        cameraBtn.innerHTML = "Turn Camera Off";
    }
    else if(cameraBtn.innerHTML == "Turn Camera Off")
    {
        cameraBtn.innerHTML = "Turn Camera On";
    }
}

function detectClick(e)
{
    
}























