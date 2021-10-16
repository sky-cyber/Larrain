$(document).ready(main);

var contador = 1;

function main() {
    $(".menu_bars").click(function() {
        //$('nav').toggle();

        if (contador == 1) {
            $("nav").animate({
                left: "0"
            });
            contador = 0;
        } else {
            contador = 1;
            $("nav").animate({
                left: "-100%"
            });
        }
    });
}

$(function() {
    $(".slides").slidesjs({
        play: {
            active: true,
            // [boolean] Generate the play and stop buttons.
            // You cannot use your own buttons. Sorry.
            effect: "slide",
            // [string] Can be either "slide" or "fade".
            interval: 4000,
            // [number] Time spent on each slide in milliseconds.
            auto: true,
            // [boolean] Start playing the slideshow on load.
            swap: true,
            // [boolean] show/hide stop and play buttons
            pauseOnHover: false,
            // [boolean] pause a playing slideshow on hover
            restartDelay: 2500
                // [number] restart delay on inactive slideshow
        }
    });
});

//codigo para validar rut
function checkRut(rut) {
    // Despejar Puntos
    var valor = rut.value.replace(".", "");
    // Despejar Guión
    valor = valor.replace("-", "");

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();

    // Formatear RUN
    rut.value = cuerpo + "-" + dv;

    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 7) {
        rut.setCustomValidity("RUT Incompleto");
        return false;
    }

    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;

    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {
        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);

        // Sumar al Contador General
        suma = suma + index;

        // Consolidar Múltiplo dentro del rango [2,7]
        if (multiplo < 7) {
            multiplo = multiplo + 1;
        } else {
            multiplo = 2;
        }
    }

    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);

    // Casos Especiales (0 y K)
    dv = dv == "K" ? 10 : dv;
    dv = dv == 0 ? 11 : dv;

    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) {
        rut.setCustomValidity("RUT Inválido");
        return false;
    }

    // Si todo sale bien, eliminar errores (decretar que es válido)
    rut.setCustomValidity("");
}

$(document).ready(function() {
    $('input[name="telefono"]').keyup(function(e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value.replace(/\D/g, "");
        }
    });
    $("#rut").keypress(function(e) {
        var regex = new RegExp("^[0-9kK]+$");
        var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
        if (regex.test(str)) {
            return true;
        }
        e.preventDefault();
        return false;
    });
    $("#nombre").keypress(function(e) {
        var regex = new RegExp("^[a-zA-Z ]+$");
        var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
        if (regex.test(str)) {
            return true;
        }
        e.preventDefault();
        return false;
    });
    jQuery.extend(jQuery.validator.messages, {
        required: "Este campo es obligatorio.",
        remote: "Please fix this field.",
        email: "Porfavor ingrese un correo valido.",
        url: "Please enter a valid URL.",
        date: "Please enter a valid date.",
        dateISO: "Please enter a valid date (ISO).",
        number: "Please enter a valid number.",
        digits: "Please enter only digits.",
        creditcard: "Please enter a valid credit card number.",
        equalTo: "Please enter the same value again.",
        accept: "Please enter a value with a valid extension.",
        maxlength: jQuery.validator.format(
            "Por favor Ingrese no mas de {0} caracteres."
        ),
        minlength: jQuery.validator.format(
            "Por favor Ingrese no menos de {0} characters."
        ),
        rangelength: jQuery.validator.format(
            "Please enter a value between {0} and {1} characters long."
        ),
        range: jQuery.validator.format("Please enter a value between {0} and {1}."),
        max: jQuery.validator.format("Por favor Ingrese no mas de {0} caracteres."),
        min: jQuery.validator.format(
            "Por favor Ingrese no menos de {0} caracteres."
        )
    });

    $("#validar")
        .submit(function(e) {
            e.preventDefault();
        })
        .validate({
            debug: true,
            rules: {
                rut: {
                    required: true
                },
                nombre: {
                    required: true
                },
                email: {
                    required: true,
                    email: true
                },
                telefono: {
                    required: true
                },
                mensaje: {
                    required: true,
                    number: true,
                    maxlength: 255
                }
            },
            messages: {
                rut: {
                    required: "Introduce tu rut."
                },
                nombre: {
                    required: "Apellido obligatorio."
                },
                email: {
                    required: "Apellido obligatorio."
                },
                telefono: {
                    required: "Introduce tu correo.",
                    email: ""
                },
                mensaje: {
                    required: "Introduce tu código postal.",
                    number: "Introduce un código postal válido.",
                    maxlength: "Debe contener 5 dígitos.",
                    minlength: "Debe contener 5 dígitos."
                }
            }
        });
});

$(".galeria__img").click(function(e) {
    var img = e.target.src;
    var pantalla =
        '<div class="modal"><img src="' +
        img +
        '" class="modal__img"><div class="modal__boton">X</div></div>';
    $("body").append(pantalla);

    $(".modal__boton").click(function() {
        $(".modal").remove();
    });
});

$(document).keyup(function(e) {
    if (e.which == 27) {
        $(".modal").remove();
    }
});