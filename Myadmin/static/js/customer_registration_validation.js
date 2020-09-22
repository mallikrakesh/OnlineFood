function checkContact()
{
    var contact = document.getElementById('input_contact').value;
    var val = 'cname='+ contact;
    var request = new XMLHttpRequest();
    request.onreadystatechange = checkContactNo;
    request.open('POST','http://127.0.0.1:8000/checkcontact/',true)
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
    request.send(val)

    function checkContactNo()
    {
        if (request.readyState === 4 && request.status ===200)
        {
            var json_data = JSON.parse(request.responseText)
            var span_id =document.getElementById('span_contact')
            var button_id =document.getElementById('btn')
            if (json_data.error !== undefined)
            {
                span_id.innerText = json_data.error;
                span_id.style.color = 'red';
                button_id.disabled = true;
            }
            else {
                 span_id.innerText = json_data.success;
                span_id.style.color = 'green';
                button_id.disabled = false;
            }
        }
    }

}