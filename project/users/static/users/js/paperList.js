
const postsBox = document.getElementById('posts-box')
console.log(postsBox)
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 3 
var responseArr = []


    $.ajax({
        type: 'GET',
        url: '/json/',
        success: function(response){
            // maxSize = response.max
            responseArr= response.data
            buildTable(responseArr)

            for (var i=0; i<responseArr.length; i++) {
                var row = $(
                    '<tr><td>' + responseArr[i].paperLink + 
                    '</td><td>' + responseArr[i].paperName + 
                    '</td><td>' + responseArr[i].paperType + 
                    '</td><td>' + responseArr[i].paperPublishDate +
                    '</td><td>' + responseArr[i].paperDescription + 
                    '</td></tr>' );
                
                    $('achivementTable').append(row);
            }
            console.log(responseArr)
            const data = response.data
            
        },
        error: function(error){
            console.log(error)
        }
    })


    function buildTable(data){

		var table = document.getElementById('achivementTable')

		for (var i = 0; i < data.length; i++){
			var row = `<tr>
							
							<td >${data[i].paperLink}</td>
							<td >${data[i].paperName}</td>
                            <td >${data[i].paperType}</td>
                            <td>${data[i].paperPublishDate}</td>
                            <td>${data[i].paperDescription}</td>
                            
					  </tr>`
			table.innerHTML += row


		}
	}




// const handleGetData = () => {
//     $.ajax({
//         type: 'GET',
//         url: '/json/',
//         success: function(response){
//             // maxSize = response.max
//             responseArr= response
//             console.log(responseArr)
//             const data = response.data
//             spinnerBox.classList.remove('not-visible')
//             setTimeout(()=>{
//                 spinnerBox.classList.add('not-visible')
//                 data.map(post=>{
//                     console.log(post.id)
//                     postsBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
//                                                 ${post.name}
//                                                 <br>
//                                                 ${post.body}
//                                             </div>`
//                 })
//                 if(maxSize){
//                     console.log('done')
//                     loadBox.innerHTML = "<h4>No more posts to load</h4>"
//                 }
//             }, 500)
//         },
//         error: function(error){
//             console.log(error)
//         }
//     })
// }

// handleGetData()

// loadBtn.addEventListener('click', ()=>{
//     visible += 3
//     handleGetData()
// })