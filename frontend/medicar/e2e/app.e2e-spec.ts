import { MedicarPage } from './app.po';

describe('medicar App', function() {
  let page: MedicarPage;

  beforeEach(() => {
    page = new MedicarPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
