
function MapSituationController($scope, $http) {
    $http.post('/api/situation/').success(function(data) {
        $scope.situation = data;
    });
}