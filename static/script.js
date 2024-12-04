// eslint-disable-next-line no-unused-vars
function toggle() {
  const hiddenDiv = document.getElementById('mobile-hidden-nav-links1')
  const line1 = document.getElementById('line1')
  const line2 = document.getElementById('line2')

  if (hiddenDiv.style.display === 'none') {
    hiddenDiv.style.display = 'block'

    line1.style.transform = 'rotate(225deg)'
    line1.style.position = 'relative'
    line1.style.top = '8px'
    line2.style.transform = 'rotate(125deg)'
    line2.style.position = 'relative'
    line2.style.bottom = '2px'
  } else {
    hiddenDiv.style.display = 'none'
    // dropdowndivs.style.margin = ' 10px 4px'
    line1.style.transform = 'rotate(180deg)'
    line2.style.transform = 'rotate(180deg)'
  }
}
