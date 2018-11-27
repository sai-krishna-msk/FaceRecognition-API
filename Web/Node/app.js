var base64Img = require('base64-img');
var sa = require('superagent');

var data = base64Img.base64Sync('test.jpg');

sa.post('https://da4358df.ngrok.io/ec/node/test')
  .send({key: data})
  .end(function(err, res) {
    console.log(JSON.stringify(res.text));
  });
//console.log(data)