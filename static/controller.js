var app = angular.module('app', ['ngRoute']);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/templates/login_page.html',
        controller:'login_page_ctrl'
    }).
      when('/login', {
        templateUrl: 'static/templates/after_login.html',
        controller:'after_login_ctrl'
    })
      // .otherwise({
      //   redirectTo: '/'
      // });
}]);

app.controller('login_page_ctrl', function ($scope,$http) {
	
})


app.controller('after_login_ctrl', function ($scope,$http) {
	$scope.loginpage_submit=function(){
		console.log($scope.admin)
	}
})

