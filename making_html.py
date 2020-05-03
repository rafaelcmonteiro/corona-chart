def drawing_html(x_labels, y_labels, coordinates):
    first_part = '''
    <html>
    <style>
        body {
          font-family: 'Open Sans', sans-serif;
        }
        
        .graph .labels.x-labels {
          text-anchor: middle;
        }
        
        .graph .labels.y-labels {
          text-anchor: end;
        }
        
        
        .graph {
          height: 800px;
          width: 1000px;
        }
        
        .graph .grid {
          stroke: #ccc;
          stroke-dasharray: 0;
          stroke-width: 1;
        }
        
        .labels {
          font-size: 13px;
        }
        
        .label-title {
          font-weight: bold;
          text-transform: uppercase;
          font-size: 12px;
          fill: black;
        }
        
        .data {
          fill: red;
          stroke-width: 1;
        }
    </style>
    
    <body>
        <svg version="1.2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="graph" aria-labelledby="title" role="img">
          <title id="title">A line chart showing some information</title>
            <g class="grid x-grid" id="xGrid">
              <line x1="0" x2="0" y1="0" y2="500"></line>
              <line x1="700" x2="700" y1="0" y2="500"></line>
            </g>
            <g class="grid y-grid" id="yGrid">
              <line x1="0" x2="700" y1="0" y2="0"></line>
              <line x1="0" x2="700" y1="500" y2="500"></line>
            </g>
          <g class="labels x-labels">

    '''
    for label in x_labels:
        first_part += label
    first_part += '''
        </g>
        <g class="labels y-labels">
        <text x="400" y="570" class="label-title">Dia</text>
        </g>
    
        <g class="labels y-labels">
    '''

    for label in y_labels:
        first_part += label

    first_part += '''
      </g>
          <g class="nada">
              <line x1="0" y1="437" x2="700" y2="437" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="375" x2="700" y2="375" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="312" x2="700" y2="312" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="250" x2="700" y2="250" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="187" x2="700" y2="187" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="125" x2="700" y2="125" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
              <line x1="0" y1="62" x2="700" y2="62" style="stroke:rgb(0,0,0, 0.3);stroke-width:2"/>
    '''

    for label in coordinates:
        first_part += label

    first_part += '''
        </g>
        </svg>
        </body>
        </html>        
    '''
    return first_part


def save_html(name, data):
    with open(f'{name}.html', 'w') as f:
        f.write(data)
