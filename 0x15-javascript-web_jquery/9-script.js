// JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$('document').ready(function (){ 
  $.getJSON(url, function (response) {
  $('DIV#hello').text(response.hello);
  });
});
