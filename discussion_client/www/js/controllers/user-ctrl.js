DiscussApp.controller('UserCtrl', ['$scope', '$state', 'UserService', function($scope, $state, UserService){
	
	$scope.friends = [];
	UserService.getFriends(function(response){
		if(response.success){
			$scope.friends = response.result;
		}
	});
}]);