$(document).ready(function() {

    const client = new $.RestClient('/api/');

    client.add('products');

    let request = client.products.read();

    request.done(function (data, textStatus, xhrObject){
      //alert('I have data: ' + data);
      console.log(data);
      $("#fruits").mirandajs(data);

      $("#fruits").mirandajs(data, {
                containers:['fruits'],
                jsonNode:['fruits'],
                effect: 'slideDown',
                delay: 2000,
                nodeDelay: 1000
            });
    });

    // OR simply:
    client.products.read().done(function (data){
      //alert('I have data: ' + data);
      console.log(data);
    });

});
