
        $(function(){
        var sampleTags = ['Data Science', 'Python', 'Android', 'Java', 'C++', 'Data Analytics', 'Big Data', 'Graphics'];
            // Single field
            //-------------------------------
            // $('#singleFieldTags').tagit({
            //     availableTags: sampleTags,
            //     // This will make Tag-it submit a single form value, as a comma-delimited field.
            //     singleField: true,
            //     singleFieldNode: $('#tag')
            // });
            $('#tag').tagit({
                availableTags: sampleTags
            });
            //-------------------------------
            // Preloading data in markup
            //-------------------------------
            //-------------------------------
            // Tag events
            //-------------------------------
            // var eventTags = $('#eventTags');
            // var addEvent = function(text) {
            //     $('#events_container').append(text + '<br>');
            // };
            // eventTags.tagit({
            //     availableTags: sampleTags,
            //     beforeTagAdded: function(evt, ui) {
            //         if (!ui.duringInitialization) {
            //             addEvent('beforeTagAdded: ' + eventTags.tagit('tagLabel', ui.tag));
            //         }
            //     },
            //     afterTagAdded: function(evt, ui) {
            //         if (!ui.duringInitialization) {
            //             addEvent('afterTagAdded: ' + eventTags.tagit('tagLabel', ui.tag));
            //         }
            //     },
            //     beforeTagRemoved: function(evt, ui) {
            //         addEvent('beforeTagRemoved: ' + eventTags.tagit('tagLabel', ui.tag));
            //     },
            //     afterTagRemoved: function(evt, ui) {
            //         addEvent('afterTagRemoved: ' + eventTags.tagit('tagLabel', ui.tag));
            //     },
            //     onTagClicked: function(evt, ui) {
            //         addEvent('onTagClicked: ' + eventTags.tagit('tagLabel', ui.tag));
            //     },
            //     onTagExists: function(evt, ui) {
            //         addEvent('onTagExists: ' + eventTags.tagit('tagLabel', ui.existingTag));
            //     }
            // });
        });