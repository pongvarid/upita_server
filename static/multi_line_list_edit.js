





    //
    jQuery(document).ready(  ($)=> {
          var value_changed = function(jQel) {
        $(".action-select").each(function( i ) {
           // console.log($(this).is(":checked"))
            if ($(this).is(":checked")) {
                 var value = jQel.val();
                 console.log('value',value);
                 $('td.field-agency select').val(value);
            }
        });

    };


        $('#result_list td.field-agency select').change(function () {
           // console.log($(this))
            value_changed($(this));
        });
        // $('#result_list td.field-importance input').keyup(function () {
        //     value_changed($(this));
        // });
    });



// jQuery(document).ready(function($){
//         var value_changed = function(jQel) {
//          var value = jQel.val();
//             $('#result_list tr').each(function () {
//
//                 if ($(this).find('#result_list td.action-checkbox input:checked').length){
//                     $('#result_list td.field-agency select').val(value)
//                      // $(this).find('td.field-agency select').val(value);
//                 }
//
//
//             });
//     };
//
//     // $('#result_list td.action-checkbox input').prop('checked', true);
//
//
//        $('#result_list td.field-agency select').change(function () {
//            console.log($(this).find('#result_list td.field-agency select').val())
//            // value_changed($(this))
//            //      console.log($(this).val())
//            let cc = $(this).val()
//             $('#result_list td.field-agency select').val($(this).val())
//             // $('#result_list tr').each(function () {
//             //
//             //     if ($('#result_list td.action-checkbox input:checked').length){
//             //          console.log('[value]',$('#result_list td.action-checkbox input').is(":checked"))
//             //         console.log('sss',cc)
//             //          $('#result_list td.field-agency select').val($(this).val())
//             //         //  // $(this).find('td.field-agency select').val(value);
//             //     }
//             // });
//
//         });
//         $('#result_list td.field-agency select').keyup(function () {
//
//         });
// });