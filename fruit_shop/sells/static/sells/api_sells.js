$(document).ready(function () {

    const restClient = new $.RestClient('/api/');
    restClient.add('sells');

    $('#listCart').click(function (e) {
        e.preventDefault();
        loadCartList();
    });

    function loadCartList() {
        console.log("loadCartList");
        $.ajax({
            url: "/sells/rest/ajax_get_cart_list",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                RestloadCartList();

            }
        });
    }

    function RestloadCartList() {
        let getCarts = restClient.sells.read();
        getCarts.done(function (data, textStatus, xhrObject) {
            console.log(data);
            $("#fruits").mirandajs(data);
            $("#fruits").mirandajs(data, {
                containers: ['fruits'],
                jsonNode: ['fruits'],
                effect: 'slideDown',
                delay: 2000,
                nodeDelay: 1000
            });
            $('a.fruitDetail').click(function (e) {
                e.preventDefault();
                let el = $(this);
                loadFruitDetail(el.data('id'))
            });
            $('button.addToCart').click(function (e) {
                e.preventDefault();
                let el = $(this);
                //loadFruitDetail(el.data('id'));
                console.log(el.data('id'));
            });
        });
    }

    function RestAddToCart(data) {
        let createProduct = restClient.sells.create(data, {});
        createProduct.done(function (data, textStatus, xhrObject) {
            $("#formFruit").html(data);
        });
    }

    function loadFruitDetail(id) {
        $.ajax({
            url: "/products/rest/ajax_get_fruit_detail",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                restLoadFruitDetail(id);
            }
        })
    }

    function restLoadFruitDetail(id) {
        let getProduct = restClient.products.read(id);
        getProduct.done(function (data, textStatus, xhrObject) {
            console.log(data);
            $("#fruit").mirandajs(data);
            $("#fruit").mirandajs(data, {
                containers: ['fruit'],
                jsonNode: ['fruit'],
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
            success: function (response) {
                $("#FruitContent").html(response);
                $('#postProduct').click(function (e) {
                    e.preventDefault();
                    let data = getFormData($('#fruitForm'));
                    RestCreateFruit(data);

                })
            }
        })
    }

    function RestCreateFruit(data) {
        let createProduct = restClient.products.create(data, {});
        createProduct.done(function (data, textStatus, xhrObject) {
            $("#formFruit").html(data);
        });
    }

    function getFormData($form) {
        var unindexed_array = $form.serializeArray();
        var indexed_array = {};

        $.map(unindexed_array, function (n, i) {
            indexed_array[n['name']] = n['value'];
        });

        return indexed_array;
    }

    function getFruitDetail(id) {
        console.log('fruit: ' + id);

    }


});
