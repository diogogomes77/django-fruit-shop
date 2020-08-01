$(document).ready(function() {

    const client = new $.RestClient('/api/');

    client.add('products');

    let getProducts = client.products.read();

    getProducts.done(function (data, textStatus, xhrObject){
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
    //client.products.read().done(function (data){
      //alert('I have data: ' + data);
    //  console.log(data);
    //});

    $('#addFruit').click(function (e) {
        console.log("addFruit click");
        e.preventDefault();
        $.ajax({
            url: "/products/rest/ajax_get_form",
            type: "get",
            success: function(response) {
              // response is form in html format
              $("#formFruit").html(response);
              $('#addFruit').toggle();
              $('#postProduct').click(function (e) {
                    console.log("click");
                    e.preventDefault();
                    let data = getFormData($('#fruitForm'));
                    //console.log(data);
                    let createProduct = client.products.create(data, {});
                    createProduct.done(function (data, textStatus, xhrObject){
                        console.log(data);
                        $("#formFruit").html(data);
                    });
                })
            }
        })

    });

    function getFormData($form){
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};

        $.map(unindexed_array, function(n, i){
            indexed_array[n['name']] = n['value'];
        });

        return indexed_array;
    }



});
