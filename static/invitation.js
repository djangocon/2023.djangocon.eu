 const download = document.querySelector("#download");
    const loader = document.querySelector("#loading");
    // showing loading
    function displayLoading() {
      loader.classList.add("display");
    }

    // hiding loading 
    function hideLoading() {
      loader.classList.remove("display");
    }

    async function start(ev) {
      ev.preventDefault();
      $("#inprogress").show();
      const form = new FormData(ev.target);
      const fullname = form.get("fullname");
      const address = form.get("address");
      const dob = form.get("dob");
      const lettertype = form.get("letterselection");
      const og = form.get("og");
      const speaker = form.get("talk");
      const passport_no = form.get("passport_no");
      var data 

      displayLoading();

      if (lettertype == "none") {
      data = {
        "fullname": fullname,
        "address": address,
        "dob": dob,
        "passport_no": passport_no
      }

      } else if (lettertype == "og") {
       data = {
            "fullname": fullname,
            "address": address,
            "dob": dob,
            "passport_no": passport_no,
            "letteropt": {
              "key": "og",
              "value": og
            }
          };
      } else if (lettertype == "speaker") {
          data = {
            "fullname": fullname,
            "address": address,
            "dob": dob,
            "passport_no": passport_no,
            "letteropt": {
              "key": "speaker",
              "value": speaker
            }
          };
      }
     
      displayLoading()
      $("#form").hide();
      await fetch('https://djc-letter.herokuapp.com/invitation', {
        method: 'POST',
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(data)
      }).then(res => res.json()).then(data => {
        hideLoading()
        console.log(data)
        $("#inprogress").hide();
        $("#ready").show();
        $("#download").show();
        download.href = data['invite_link']

      });
    }

    $(document).ready(function () {
      $("#letterselection").change(function () {
        var selected = $(this).val();
        if (selected == "attendee") {
          $("#og").hide();
          $("#speaker").hide();
        }
        else if (selected == "og") {
          $("#og").show();
          $("#speaker").hide();
        }
        else if (selected == "speaker") {
          $("#og").hide();
          $("#speaker").show();
        }
      });
    });

    start();