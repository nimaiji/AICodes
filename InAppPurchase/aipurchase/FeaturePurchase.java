package aipurchase;

import java.util.List;

public abstract class FeaturePurchase {

    public enum Scope {
        HIGH_CHANCE,
        SHOW,
        PROMOTION,
        DOWN,
        SINUSOID
    }

    protected int MIN_AVG;
    protected int MAX_AVG;
    protected int GROWTH;
    private float currentAvg;
    private int acc = 0;
    private int periodAcc = 0;
    private int index = 0;
    private Scope scope;
    private List<Object> periodItems;
    private OnScopeHappened onScopeHappened;
    private SaveFeatureInterface saveFeature;
    private Logger logger = null;

    public FeaturePurchase(int minAvg, int maxAvg, int growth) {
        MIN_AVG = minAvg;
        MAX_AVG = maxAvg;
        GROWTH = growth;
        currentAvg = (MIN_AVG + MAX_AVG) / 2;
    }

    public void query(int feature, Object item){
        if (feature > 0) {
            periodItems.add(item);
            index++;
            logger.Log("Add new item with feature",String.valueOf(feature));
        } else if (feature < 0 && periodItems.contains(item)) {
            periodItems.remove(item);
            index--;
            logger.Log("Remove an item with feature",String.valueOf(feature));
        } else if (feature != 0) {
            return;
        }

        acc += feature;
        periodAcc += feature;
        float diff = periodAcc - currentAvg;

        if (diff > GROWTH && currentAvg == MAX_AVG) {
            onScopeHappened.highChance();
            scope = Scope.HIGH_CHANCE;
            logger.Log("Scope","High chance to sell");
        } else if (diff <= -MIN_AVG && currentAvg == MIN_AVG) {
            onScopeHappened.promotion();
            scope = Scope.PROMOTION;
            logger.Log("Scope","Need promotion");
        } else if (diff > GROWTH) {
            onScopeHappened.show();
            scope = Scope.SHOW;
            logger.Log("Scope","Show offers");
        } else if (diff <= -GROWTH) {
            onScopeHappened.down();
            scope = Scope.DOWN;
            logger.Log("Scope","Doesn't use your app");
        } else {
            onScopeHappened.sinusoid();
            scope = Scope.SINUSOID;
            logger.Log("Scope","There isn't any growth");
        }
    }

    public Scope getScope() {
        return scope;
    }

    public void update() {
        currentAvg = acc / index;
        if (saveFeature.save())
            logger.Log("Save","Data saved successfully");
        else
            logger.Log("Save","There is a problem in saving data");
        saveFeature.resetOnPeriod();
        logger.Log("Reset","All data resets");
    }

    public void setOnScopeHappened(OnScopeHappened onScopeHappened) {
        this.onScopeHappened = onScopeHappened;
    }

    public void setLogger(Logger logger) {
        this.logger = logger;
    }

    
}
