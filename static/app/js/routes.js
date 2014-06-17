define(['angular', 'app'], function(angular, app) {
	'use strict';

	return app.config(['$routeProvider', function($routeProvider) {
		$routeProvider.when('/view1', {
			templateUrl: '/static/app/partials/partial1.html',
			controller: 'MyCtrl1'
		});
		$routeProvider.when('/view2', {
			templateUrl: '/static/app/partials/partial2.html',
			controller: 'MyCtrl2'
		});
		$routeProvider.otherwise({redirectTo: '/view1'});
	}]);

});