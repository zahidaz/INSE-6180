📦
997 /src/index.js.map
858 /src/index.js
✄
{"version":3,"file":"index.js","sourceRoot":"/Users/zahid/Downloads/shared/privacy and data mining/tracer/","sources":["src/index.ts"],"names":[],"mappings":"AAAA,IAAI,CAAC,OAAO,CAAC,GAAG,EAAE;IAEd,MAAM,WAAW,GAAG,IAAI,CAAC,GAAG,CAAC,yBAAyB,CAAC,CAAC;IACxD,MAAM,KAAK,GAAG,IAAI,CAAC,GAAG,CAAC,kBAAkB,CAAC,CAAC;IAC3C,WAAW,CAAC,QAAQ,CAAC,cAAc,GAAG;QAClC,kBAAkB,EAAE,CAAC;QACrB,IAAI,CAAC,QAAQ,EAAE,CAAC;IACpB,CAAC,CAAC;IAEH,MAAM,QAAQ,GAAG,IAAI,CAAC,GAAG,CAAC,sBAAsB,CAAC,CAAC;IAClD,QAAQ,CAAC,OAAO,CAAC,cAAc,GAAG;QAC9B,iBAAiB,EAAE,CAAC;QACpB,IAAI,CAAC,OAAO,EAAE,CAAC;IACnB,CAAC,CAAA;IAED,QAAQ,CAAC,QAAQ,CAAC,cAAc,GAAG;QAC/B,kBAAkB,EAAE,CAAC;QACrB,IAAI,CAAC,QAAQ,EAAE,CAAC;IACpB,CAAC,CAAA;IAEA,SAAS,iBAAiB;QACtB,KAAK,CAAC,iBAAiB,EAAE,CAAC;QAC1B,OAAO,CAAC,GAAG,CAAC,wBAAwB,CAAC,CAAC;IAC1C,CAAC;IAED,SAAS,kBAAkB;QACvB,MAAM,QAAQ,GAAG,QAAQ,GAAG,IAAI,IAAI,EAAE,CAAC,OAAO,EAAE,GAAG,QAAQ,CAAC;QAC5D,KAAK,CAAC,kBAAkB,CAAC,QAAQ,CAAC,CAAC;QACnC,OAAO,CAAC,GAAG,CAAC,wBAAwB,CAAC,CAAC;IAC1C,CAAC;AAEL,CAAC,CAAC,CAAC"}
✄
Java.perform(() => {
    const Application = Java.use('android.app.Application');
    const Debug = Java.use('android.os.Debug');
    Application.onCreate.implementation = function () {
        startMethodTracing();
        this.onCreate();
    };
    const Activity = Java.use('android.app.Activity');
    Activity.onPause.implementation = function () {
        stopMethodTracing();
        this.onPause();
    };
    Activity.onResume.implementation = function () {
        startMethodTracing();
        this.onResume();
    };
    function stopMethodTracing() {
        Debug.stopMethodTracing();
        console.log('Method Tracing stopped');
    }
    function startMethodTracing() {
        const fileName = "trace_" + new Date().getTime() + '.trace';
        Debug.startMethodTracing(fileName);
        console.log('Method Tracing started');
    }
});