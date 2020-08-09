$(document).ready(function () {


    const restClient = new $.RestClient('/api/', {"ajax": getAjaxOption()});
    restClient.add('products');
    restClient.add('sells');
    restClient.add('carts');
    restClient.carts.add('items');

    let mycart = null;

    if (is_authenticated && !is_staff){
        GetMyCart();
    }

    loadFruitList();

    function GetMyCart() {
        console.log('GetMyCart');
        let cart = restClient.carts.read('mycart');
        cart.done(function (data, textStatus, xhrObject) {
            console.log(data);
            setMyCart(data);
        });
    }

    function setMyCart(cart){
        console.log('setMyCart');
        console.log(cart);
        mycart = cart;
        $("#cartItems").mirandajs(cart['items']);
        /*$("#cartItems").mirandajs(cart['items'], {
            containers: ['cartItems'],
            jsonNode: ['cartItems'],
            effect: 'slideDown',
            delay: 2000,
            nodeDelay: 1000
        });*/
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
            url: "/products/ajax_get_fruit_list",
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
            /*$("#fruits").mirandajs(data, {
                containers: ['fruits'],
                jsonNode: ['fruits'],
                effect: 'slideDown',
                delay: 2000,
                nodeDelay: 1000
            });*/
            $('a.fruitDetail').click(function (e) {
                e.preventDefault();
                let el = $(this);
                loadFruitDetail(el.data('id'))
            });
            $('button.editFruit').click(function (e) {
                e.preventDefault();
                let el = $(this);
                editFruit(el.data('id'))
            });
            $('button.deleteFruit').click(function (e) {
                e.preventDefault();
                let el = $(this);
                deleteFruit(el.data('id'))
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
        console.log('RestAddToCart');
        data = {
            'cart': mycart['id'],
            'product': product_id,
            'quantity': 1
        };
        let addItem = restClient
            .carts.items
            .create(mycart['id'], data, {});
        addItem.done(function (data, textStatus, xhrObject) {
            console.log(data);
            setMyCart(data);
        });
    }

    function deleteItem(item_id) {
        console.log('deleteItem cart: ' + mycart['id'] + " item:" + item_id);
        let deleteItem = restClient
            .carts.items
            .del(mycart['id'], item_id);
        deleteItem.done(function (data, textStatus, xhrObject) {
            console.log(data);
            setMyCart(data);
        });
    }


    function loadFruitDetail(id) {
        $.ajax({
            url: "/products/ajax_get_fruit_detail",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                restLoadFruitDetail(id);
            }
        })
    }

    function editFruit(id) {
        $.ajax({
            url: "/products/ajax_get_fruit_edit_form",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                restLoadFruitEdit(id);

            }
        })
    }
    function restLoadFruitEdit(id) {
        console.log('restLoadFruitEdit');
        let getProduct = restClient.products.read(id);
        getProduct.done(function (data, textStatus, xhrObject) {
            console.log(data);
            $("#fruit").mirandajs(data);
            $('button.putProduct').click(function (e) {
                e.preventDefault();
                console.log('putProduct');
                let el = $(this);
                let data = getFormData($('#fruitForm'));
                console.log(data);
                restSaveFruitEdit(el.data('id'), data)
            });
        });
    }

    function restSaveFruitEdit(id, data) {
        let putProduct = restClient.products.update(id, data);
        putProduct.done(function (data, textStatus, xhrObject) {
            console.log(data);
            $("#fruit").mirandajs(data);
            loadFruitList();
        });
    }

    function deleteFruit(id) {
        restClient.products.del(id);
        loadFruitList();

    }

    function restLoadFruitDetail(id) {
        let getProduct = restClient.products.read(id);
        getProduct.done(function (data, textStatus, xhrObject) {
            console.log(data);
            $("#fruit").mirandajs(data);
        });
    }

    function loadFruitForm() {
        $.ajax({
            url: "/products/ajax_get_fruit_form",
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

    function loadFruitCategoryForm() {
        $.ajax({
            url: "/products/ajax_get_fruit_category_form",
            type: "get",
            success: function (response) {
                $("#FruitContent").html(response);
                $('#postProductCategory').click(function (e) {
                    e.preventDefault();
                    let data = getFormData($('#fruitCategoryForm'));
                    RestCreateFruitCategory(data);

                })
            }
        })
    }

    function RestCreateFruit(data) {
        let createProduct = restClient.products.create(data, {});
        createProduct.done(function (data, textStatus, xhrObject) {
            $("#formFruit").html(data);
            loadFruitList();
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
