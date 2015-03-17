DiscussApp.controller('TopicsCtrl', ['$scope', 'TopicService', function($scope, TopicService){

	var ctrlData = {};

	TopicService.getAllTopics()
	.then(function(topics){
		ctrlData.topics = topics;
		$scope.data = ctrlData;
		console.log($scope.data);
	});
}]);