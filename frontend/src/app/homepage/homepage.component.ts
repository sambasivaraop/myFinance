import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  @Input() public userData;
  public menuClick = false;
  constructor(private _router: Router) { }

  ngOnInit() {
    this._router.navigate(['/']);
  }

  onHomeClick(){
      this.menuClick = false;
      this._router.navigate(['/']);
    }

  onMenuClick(){
    this.menuClick = true;
  }

}
