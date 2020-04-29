// https://www.youtube.com/watch?v=3GqUM4mEYKA
window.addEventListener('load', (x, y) => {
  console.log('hello there!');
  const canvas = document.querySelector('#myCanvas');
  const ctx = canvas.getContext('2d');

  // Resizing
  canvas.height = 250;
  canvas.width = 250;

  // A comment on answer https://stackoverflow.com/q/33910742 for below two lines
  ctx.fillStyle = 'white';
  ctx.fillRect(0,0,canvas.width,canvas.height);

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
    ctx.lineWidth = 20;
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

var pkid;

function feedback() {
  let x = document.getElementById("userSuggestion").value;
  $.ajax({type: 'POST',
                url: '/feedback/',                            // some data url
                data: {suggestion: 'x', keyid: 'pkid'},       // some params  
                success: function (response) {                  // callback
                    if (response.result === 'OK') {
                        if (response.data && typeof(response.data) === 'object') {
                            // do something with the successful response.data
                            // e.g. response.data can be a JSON object
                        }
                    } else {
                        // handle an unsuccessful response
                    }
                }
               });
}


// https://www.codicode.com/art/upload_and_save_a_canvas_image_to_the_server.aspx
function UploadPic() {
    // Generate the image data
  let Pic = document.getElementById("myCanvas").toDataURL("image/png");
  Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "");

  console.log('I have the image here will submit now!');

  /* Discarding this method of interacting with server to avoid turning async to false
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
  result.innerHTML = "Eve thinks you entered " + obj.prediction; // */

  jQuery.ajax({
    type: 'POST',
    url: 'upload/',
    // data: data,
    data: '{"file": "' + Pic + '", "remark": "My Canvas submission"}',
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    success: function(data, textStatus, jqXHR)
    {
      //data - response from server
      console.log(data);
      let result = document.getElementById("prediction");
      result.innerHTML = "Eve thinks you entered " + data.prediction;
    },
    error: function (jqXHR, textStatus, errorThrown)
    {
      console.log("Error occurred!!");
      console.log(jqXHR);
      console.log(textStatus);
      console.log(errorThrown);

    }
  });

}
