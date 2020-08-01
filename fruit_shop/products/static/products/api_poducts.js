$(document).ready(function() {

    const restClient = new $.RestClient('/api/');
    restClient.add('products');

    $('#listFruit').click(function (e){
        e.preventDefault();
        loadFruitList();
    });

    $('#addFruit').click(function (e) {
        e.preventDefault();
        loadFruitForm();
    });


    function loadFruitList(){
        console.log("loadFruitList");
        $.ajax({
            url: "/products/rest/ajax_get_fruit_list",
            type: "get",
            success: function(response) {
              $("#FruitContent").html(response);
              RestloadFruiList();
            }
        });
    }

    function RestloadFruiList(){
        let getProducts = restClient.products.read();
        getProducts.done(function (data, textStatus, xhrObject){
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
    }


    function loadFruitForm() {
        $.ajax({
            url: "/products/rest/ajax_get_fruit_form",
            type: "get",
            success: function(response) {
              $("#FruitContent").html(response);
              $('#postProduct').click(function (e) {
                    e.preventDefault();
                    let data = getFormData($('#fruitForm'));
                    RestCreateFruit(data);

                })
            }
        })
    }

    function RestCreateFruit(data){
        let createProduct = restClient.products.create(data, {});
        createProduct.done(function (data, textStatus, xhrObject){
            $("#formFruit").html(data);
        });
    }

    function getFormData($form){
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};

        $.map(unindexed_array, function(n, i){
            indexed_array[n['name']] = n['value'];
        });

        return indexed_array;
    }

    function getFruitDetail(id){
        console.log('fruit: ' + id);

    }



});
