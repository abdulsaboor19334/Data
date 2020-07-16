const path = require('path')

module.export = {
    mode: 'development',
    entry:{
        app:"./index.js"
    },
    output:{
        path: path.resolve(__dirname,'dist'),
        filename: "bundle.js"
    },
    module:{
        loaders:[{
            test: /\.js?$/,
            exclude:/node_modules/,
            loader: 'babel-loader',
            query:{
                preset:'env'
            }
        }]
    }
}