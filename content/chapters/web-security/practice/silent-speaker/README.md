# Silent Speaker

Exemplul curent arată că uneori Frontend-ul și Backend-ul trebuie neapărat să fie sincronizate.
Vom vedea în acest exemplu că deși poate clientului nu îi este expusă o funcționalitate, ea poate totuși exista în Backend.
Cu alte cuvinte, chiar dacă ceva nu e vizibil în pagină, Serverul poate expune mai mult decât lasă să se vadă.

Avem informații că pagina `http://141.85.224.104:40001/index.php` expune o vulnerabilitate de tip Local File Inclusion.

Observați că pagina nu conține nimic.
Însă inspectați cu atenție sursa paginii.
Există elemente comentate în pagină.

Încercați să exploatați acest lucru.
