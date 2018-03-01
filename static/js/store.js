/*jshint unused:false */

(function (exports) {

	'use strict';

	var STORAGE_KEY = 'todos-vuejs';



	exports.todoStorage = {
		fetch: function () {
			// return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

			var responseText = '[]';
  			var xhttp = new XMLHttpRequest();

			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					responseText = this.responseText;
				}
		  	};

			xhttp.open ('GET', 'http://python.akhundzada.az:8000/api', false);
			xhttp.send();

			return JSON.parse(responseText)
		},
		save: function (todos) {
			var updateLocalStorage = false;
			var xhttp = new XMLHttpRequest();

			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					console.log (this.responseText);
					updateLocalStorage = true;
				}
		  	};

			xhttp.open('POST', 'http://python.akhundzada.az:8000/api/update', false);
			xhttp.setRequestHeader("Content-type", "application/json");
			xhttp.send(JSON.stringify(todos));

			if (updateLocalStorage)
			{
				localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
			}

		}
	};

})(window);
