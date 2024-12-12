Java.perform(() => {

    const Application = Java.use('android.app.Application');
    const Debug = Java.use('android.os.Debug');
    Application.onCreate.implementation = function() {
        startMethodTracing();
        this.onCreate();
    };

   const Activity = Java.use('android.app.Activity'); 
   Activity.onPause.implementation = function() {
       stopMethodTracing();
       this.onPause();
   }

   Activity.onResume.implementation = function() {
       startMethodTracing();
       this.onResume();
   }

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


