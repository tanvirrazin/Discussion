DiscussApp.controller('AuthCtrl', ['$scope', '$state', 'AuthService', function($scope, $state, AuthService){

	$scope.user = {};
	$scope.login = function(){
		AuthService.login($scope.user, function(response){
			if(response.success)
				$state.go('tab.friends');
		});
	}

	$scope.logout = function(){
		AuthService.logout();
		$state.go('login');
	}
}]);