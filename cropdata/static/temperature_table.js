
"use strict";

var app = angular.module("resultViewer", []).config(function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode(true);
});

var resultController = function($scope, $log, $http, $location){
    //setting up initial varables.


    $scope.initial = {
        showPerPage: [15, 20, 50, 100, 200],
        curShowPerPage: 15,
        showFilter: false,
       // year_options: [2008, 2009, 2010, 2011, 2012, 2013],
        year_options: ['ALL'],
        default_year: 'ALL',
        district_options: ['ALL'],
        default_district: 'ALL'
    }
    $scope.config = {
        has_prev: false,
        has_next: false,
        cur_page: 0,
        total_page: null
    }

    // getting all query parameters.
    var loc = $location
    var q = loc.search().q
    var v = loc.search().v

    var store_family = '';
    var store_class = '';
    // calling pagination api.
    var onErrorAfterEdit = function(err){
        alert("last action is not successful Kindly retry");
    }
    var onError = function(err){
        $log.error(err)
        $log.info('Please copy and send this error to admin so that it can be taken care of. Thanks for your support.')
    }

    var getPaginationComplete = function(response){
        var config_dict = response.data.config
        if(config_dict.has_prev){
            $scope.config.has_prev = true;
        }else{
            $scope.config.has_prev = false;
        }

        if(config_dict.has_next){
            $scope.config.has_next = true;
        }else{
            $scope.config.has_next = false;
        }

        $scope.config.cur_page = config_dict.cur_page;
        $scope.config.total_page = config_dict.total_pages;

        $scope.temperatureList = response.data.list;
        $scope.yearList = response.data.year;
        // console.log($scope.yearList);
        $scope.districtList = response.data.district;

        $scope.initial.year_options = ['ALL'];
        $scope.initial.district_options = ['ALL'];

        $scope.initial.year_options = $scope.initial.year_options.concat($scope.yearList);
        $scope.initial.district_options = $scope.initial.district_options.concat($scope.districtList);

        //$scope.temperatureList.selected = {};
        $('#paginationStatusLoader').remove();
        $scope.dataReady = true;
    }

    $scope.pagination = function(next, startOver){
        var page = null;
        if(!startOver){
            if(next){
                page = $scope.config.cur_page + 1;
            }else{
                page = $scope.config.cur_page -1;
            }
        }else{
            page = $scope.config.cur_page
        }

        $scope.dataReady = false;
        //$('#panelData').append(dataLoader.replace('%dataLoaderId%', 'paginationStatusLoader'));
        $http({
            url: '/temperaturetableapi/?count='+$scope.initial.curShowPerPage+'&page='+page+'&year='+$scope.initial.default_year+'&district='+$scope.initial.default_district,
            method: 'GET',
        }).then(getPaginationComplete, onError);
    }
    // get detailed info functions.

    $scope.pagination(true);

    $scope.getTemplate = function (temperature_O) {

    return 'display';

    };


};

app.controller("resultController", ["$scope", "$log", "$http", "$location", resultController]);
