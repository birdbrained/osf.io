/**
 * Dataverse FileBrowser configuration module.
 */
;(function (global, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['js/rubeus'], factory);
    } else if (typeof $script === 'function') {
        $script.ready('rubeus', function() { factory(Rubeus); });
    } else { factory(Rubeus); }
}(this, function(Rubeus) {

    // Private members

    function refreshDataverseTree(grid, item, state) {
        var data = item.data || {};
        data.state = state;
        var url = item.urls.state + '?' + $.param({state: state});
        $.ajax({
            type: 'get',
            url: url,
            success: function(data) {
                // Update the item with the new state data
                $.extend(item, data[0]);
                grid.reloadFolder(item);
            }
        });
    }

    // Register configuration
    Rubeus.cfg.dataverse = {
        // Handle changing the state
        listeners: [{
            on: 'change',
            selector: '.dataverse-state-select',
            callback: function(evt, row, grid) {
                var $this = $(evt.target);
                var state = $this.val();
                refreshDataverseTree(grid, row, state);
            }
        }]
    };

}));
