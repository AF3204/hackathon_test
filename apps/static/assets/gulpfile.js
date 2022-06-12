/*

=========================================================
* AppSeed - Simple SCSS compiler via Gulp
=========================================================

*/

let autoprefixer = require('gulp-autoprefixer');
let browserSync = require('browser-sync').create();
let cleanCss = require('gulp-clean-css');
let gulp = require('gulp');
const npmDist = require('gulp-npm-dist');
let sass = require('gulp-sass')(require('node-sass'));
let wait = require('gulp-wait');
let sourcemaps = require('gulp-sourcemaps');
let rename = require("gulp-rename");

// Define COMMON paths

const paths = {
    src: {
        base: './',
        css: './css',
        scss: './sass',
        node_modules: './node_modules/',
        vendor: './vendor'
    }
};

// Compile SCSS
gulp.task('scss', function() {
    return gulp.src([paths.src.scss + '/atlantis.scss'])
        .pipe(wait(500))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            overrideBrowserslist: ['> 1%']
        }))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(paths.src.css))
        .pipe(browserSync.stream());
});

// Minify CSS
gulp.task('minify:css', function() {
    return gulp.src([
            paths.src.css + '/atlantis.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss', 'minify:css'));
