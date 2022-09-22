*** Settings ***
Library                             SeleniumLibrary
Library                             Collections


*** Keywords ***
I navigate to reqres.in
    open browser                    https://reqres.in       chrome


I get endpoint from UI
    &{dict}=         Create Dictionary
    FOR     ${i}        IN RANGE        1       15
        click element                   (//li/a)[${i}]
        ${key1}=        get text                        //span[@class="url"]
        ${value1}=      get element attribute           (//li//a/parent::li)[${i}]      data-http
        set to dictionary       ${dict}     ${key1}=${value1}
    END
#    log to console      ${dict}
#    FOR    ${key_value_tuple}    IN    &{dict}
#        Log    ${key_value_tuple}
#    END
    set global variable     ${dict}