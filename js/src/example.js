var widgets = require('jupyter-js-widgets');
var _ = require('underscore');


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including `_model_name`, `_view_name`, `_model_module`
// and `_view_module` when different from the base class.
//
// When serialiazing entire widget state for embedding, only values different from the
// defaults will be specified.
var AnimationModel = widgets.DOMWidgetModel.extend({
	defaults: _.extend({}, widgets.DOMWidgetModel.prototype.defaults, {
		_model_name : 'AnimationModel',
		_view_name : 'AnimationView',
		_model_module : 'animation-widget',
		_view_module : 'animation-widget',
		value : 0.0,
		run: false,
		period: 5000.0,
		nbsamples: 100,
		loop: false
	})
});


// Custom View. Renders the widget model.
var AnimationView = widgets.DOMWidgetView.extend({

	// Render the view.
	render: function() { 
		this.value_changed();
		this.model.on('change:value', this.value_changed, this);
		this.model.on('change:run', this.set_trigger, this);
		this.timerId = 0;
		this.last_update_date = 0;
	},

	value_changed: function() {
		this.$el.text(this.model.get('value')); 
	},

	increment_val: function(widget)
        {
            var period = widget.model.get('period')
            var nbsamples = widget.model.get('nbsamples')
            
	    var d = new Date();
	    var new_date = d.getTime()
	    // Compute the delta in regard to the date
            var delta = (new_date - widget.last_update_date) / period
            var value = widget.model.get('value');
            value = value + delta;
            widget.touch();
	    // Set the new date
	    widget.last_update_date = new_date;
            widget.value_changed();
            if(widget.model.get('loop'))
	    {
		// Loop value
		while(value >= 1.0)
		{
			value = value - 1.0;
		}
	    }
	    else
	    {
 		value = Math.min(value, 1.0);
	    }
            widget.model.set('value', value);
            // Relaunch timer
            if (value < 1.0)
            {
                widget.timerId = setTimeout(widget.increment_val, period/nbsamples, widget);
            }
            else    
            {
                widget.timerId = 0;
                widget.model.set('run', false);
                widget.touch();
            }
        },
        
        set_trigger: function()
        {
            if(this.timerId)
            {
                clearTimeout(this.timerId);
                this.timerId = 0;
            }
            
            if(this.model.get('run'))
            {
                var period = this.model.get('period')
                var nbsamples = this.model.get('nbsamples')
                if (this.model.get('value') >= 1.0)
                {
                    this.model.set('value', 0.0);
                    this.value_changed();
                    this.touch();
                }
               this.timerId = setTimeout(this.increment_val, period/nbsamples, this);
	       var d = new Date();
	       this.last_update_date = d.getTime();
            }
        },
});


module.exports = {
	AnimationModel : AnimationModel,
	AnimationView : AnimationView
};
