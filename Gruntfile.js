module.exports = function(grunt){
    grunt.initConfig({
        sass:{
            dist:{
                options:{
                    style: 'compressed'
                },
                files:{
                    'static/style/main.css': 'media/assets/style/main.scss'
                }
            }
        },
        watch:{
            sass:{
                files:['media/assets/style/*.scss'],
                tasks: ['sass:dist']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['sass:dist']);
};
