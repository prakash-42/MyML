// https://www.youtube.com/watch?v=3GqUM4mEYKA

window.addEventListener('load', (x, y) => {
  console.log('hello there!');
  const canvas = document.querySelector('#myCanvas');
  const ctx = canvas.getContext('2d');

  // Resizing
  canvas.height = 250;
  canvas.width = 250;

  let painting = false;

  function  startPosition(e) {
    painting = true;
    draw(e);
  }

  function finishedPosition(){
    painting = false;
    ctx.beginPath();
  }

  function draw(e){
    if(!painting) return;
    ctx.lineWidth = 10;
    ctx.lineCap = "round";
    let xpos = getMousePos(canvas, e).x;
    let ypos = getMousePos(canvas, e).y;
    ctx.lineTo(xpos, ypos);
    ctx.stroke();
    ctx.beginPath();
    ctx.lineTo(xpos, ypos);
  }

  function getMousePos(canvas, evt) {
    const rect = canvas.getBoundingClientRect();
    return {
      x: evt.clientX - rect.left,
      y: evt.clientY - rect.top
    };
}


  // Add event listeners
  canvas.addEventListener('mousedown', startPosition);
  canvas.addEventListener('mouseup', finishedPosition);
  canvas.addEventListener('mousemove', draw);

});

// https://www.codicode.com/art/upload_and_save_a_canvas_image_to_the_server.aspx
function UploadPic() {
    // Generate the image data
  let Pic = document.getElementById("myCanvas").toDataURL("image/png");
  Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "");

  console.log('I have the image here will submit now!');

  let xhr = new XMLHttpRequest();


  let data = new FormData();
  data.append("file", Pic);
  data.append("remark", "Best Pic ever");

  // https://stackoverflow.com/a/38527398 for async = false in below line
  xhr.open('POST','upload/', false);
  xhr.setRequestHeader("contentType",  'application/json; charset=utf-8');
  xhr.send(data);
  let result = document.getElementById("prediction");
  console.log("Setting prediction result now.");
  console.log(xhr.responseText);
  let obj = JSON.parse(xhr.responseText);
  // let obj = xhr.responseText;
  console.log(typeof obj);

  let prediction = "2";
  result.innerHTML = "Eve thinks you entered " + obj.prediction;



}