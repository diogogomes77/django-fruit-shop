$(document).ready(function () {


    const restClient = new $.RestClient('/api/', {"ajax": getAjaxOption()});
    restClient.add('products');
    restClient.add('sells');
    restClient.add('carts');
    restClient.carts.add('items');

    let mycart = null;

    GetMyCart();

    function GetMyCart() {
        let mycart = restClient.carts.read('mycart');
        mycart.done(function (data, textStatus, xhrObject) {
            console.log(data);
            setMyCart(data);
        });
    }

    function setMyCart(cart){
        mycart = cart;
        $("#cartItems").mirandajs(cart['items']);
        $("#cartItems").mirandajs(cart['items'], {
            containers: ['cartItems'],
            jsonNode: ['cartItems'],
            effect: 'slideDown',
            delay: 2000,
            nodeDelay: 1000
        });
        $('button.deleteItem').click(function (e) {
                e.preventDefault();
                let el = $(this);
                console.log(el.data('id'));
                deleteItem(el.data('id'));
            });
    }

    function RestloadCartItems() {
        let items = restClient.products.read();
        items.done(function (data, textStatus, xhrObject) {
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
                RestAddToCart(el.data('id'));
            });
        });
    }

    $('#listFruit').click(function (e) {
        e.preventDefault();
        loadFruitList();
    });

    $('#addFruit').click(function (e) {
        e.preventDefault();
        loadFruitForm();
    });

    function loadFruitList() {
        console.log("loadFruitList");
        $.ajax({
            url: "/products/rest/ajax_get_fruit_list",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                RestloadFruiList();

            }
        });
    }

    function RestloadFruiList() {
        let getProducts = restClient.products.read();
        getProducts.done(function (data, textStatus, xhrObject) {
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
                RestAddToCart(el.data('id'));
            });
        });
    }

    function RestAddToCart(product_id) {
        data = {
            'cart': mycart['id'],
            'product': product_id,
            'quantity': 1
        };
        let addItem = restClient
            .carts.items
            .create(mycart['id'], data, {});
        addItem.done(function (data, textStatus, xhrObject) {
            setMyCart(data);
        });
    }

    function deleteItem(item_id) {

        let deleteItem = restClient
            .carts.items
            .del(mycart['id'], item_id);
        deleteItem.done(function (data, textStatus, xhrObject) {
            setMyCart(data);
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

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function getAjaxOption(){
        let ajaxOption = {
        beforeSend: function(xhr, settings) {
            if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        }
        };
        return ajaxOption;
    }



});
